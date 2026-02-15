#include <iostream>
#include <fstream>
#include <vector>
#include <zlib.h>

constexpr int CHUNK_SIZE = 1 << 15; // 32KB
constexpr int COMPRESSION_LEVEL = 6;

// Compress input file -> output file (.gz)
int gzip_compress(const std::string& input_path, const std::string& output_path) {
    std::ifstream in(input_path, std::ios::binary);
    if (!in) return 1;

    std::ofstream out(output_path, std::ios::binary);
    if (!out) return 1;

    z_stream strm{};
    if (deflateInit2(&strm,
                     COMPRESSION_LEVEL,
                     Z_DEFLATED,
                     15 + 16,      // 15 window bits + 16 = gzip
                     8,
                     Z_DEFAULT_STRATEGY) != Z_OK)
        return 1;

    std::vector<char> in_buffer(CHUNK_SIZE);
    std::vector<char> out_buffer(CHUNK_SIZE);

    int flush;
    do {
        in.read(in_buffer.data(), CHUNK_SIZE);
        strm.avail_in = in.gcount();
        strm.next_in = reinterpret_cast<Bytef*>(in_buffer.data());
        flush = in.eof() ? Z_FINISH : Z_NO_FLUSH;

        do {
            strm.avail_out = CHUNK_SIZE;
            strm.next_out = reinterpret_cast<Bytef*>(out_buffer.data());

            deflate(&strm, flush);

            size_t have = CHUNK_SIZE - strm.avail_out;
            out.write(out_buffer.data(), have);
        } while (strm.avail_out == 0);

    } while (flush != Z_FINISH);

    deflateEnd(&strm);
    return 0;
}

// Decompress .gz file -> output file
int gzip_decompress(const std::string& input_path, const std::string& output_path) {
    std::ifstream in(input_path, std::ios::binary);
    if (!in) return 1;

    std::ofstream out(output_path, std::ios::binary);
    if (!out) return 1;

    z_stream strm{};
    if (inflateInit2(&strm, 15 + 16) != Z_OK) // 15+16 = gzip
        return 1;

    std::vector<char> in_buffer(CHUNK_SIZE);
    std::vector<char> out_buffer(CHUNK_SIZE);

    int ret;
    do {
        in.read(in_buffer.data(), CHUNK_SIZE);
        strm.avail_in = in.gcount();
        if (strm.avail_in == 0) break;

        strm.next_in = reinterpret_cast<Bytef*>(in_buffer.data());

        do {
            strm.avail_out = CHUNK_SIZE;
            strm.next_out = reinterpret_cast<Bytef*>(out_buffer.data());

            ret = inflate(&strm, Z_NO_FLUSH);
            if (ret == Z_STREAM_ERROR) return 1;

            size_t have = CHUNK_SIZE - strm.avail_out;
            out.write(out_buffer.data(), have);
        } while (strm.avail_out == 0);

    } while (ret != Z_STREAM_END);

    inflateEnd(&strm);
    return ret == Z_STREAM_END ? 0 : 1;
}

// Entry point of the program.
// argc = number of command-line arguments
// argv = array of C-style strings containing the arguments
//
// Example execution from terminal:
//   zip.exe c input.txt output.gz
//
// In that case:
//   argc == 4
//   argv[0] = "zip.exe"          (program name)
//   argv[1] = "c"                (mode: compress)
//   argv[2] = "input.txt"        (input file path)
//   argv[3] = "output.gz"        (output file path)
int main(int argc, char* argv[]) {

    // Ensure exactly 3 user arguments are provided:
    // mode + input file + output file
    // If argc != 4, the user did not follow the expected usage format.
    if (argc != 4) {

        // Print usage instructions to standard error (std::cerr).
        // std::cerr is used for errors instead of std::cout.
        std::cerr << "Usage:\n"
                  << "  compress:   " << argv[0] << " c input output.gz\n"
                  << "  decompress: " << argv[0] << " d input.gz output\n";

        // Return non-zero to indicate failure.
        // Convention: return 0 = success, non-zero = error.
        return 1;
    }

    // argv elements are C-style strings (char*).
    // Convert them to std::string for safer and easier manipulation.
    std::string mode = argv[1];     // "c" or "d"
    std::string input = argv[2];    // input file path
    std::string output = argv[3];   // output file path

    // If mode is "c", perform compression.
    if (mode == "c")
        return gzip_compress(input, output);

    // If mode is "d", perform decompression.
    else if (mode == "d")
        return gzip_decompress(input, output);

    // If mode is neither "c" nor "d", the user provided invalid input.
    else {
        std::cerr << "Invalid mode. Use 'c' for compress or 'd' for decompress.\n";
        return 1;
    }
}
