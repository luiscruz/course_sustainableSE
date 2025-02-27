FROM ruby:2.7.4

WORKDIR /myapp
COPY . /myapp

# Manually install the last compatible RubyGems version for Ruby 2.7
RUN gem install rubygems-update -v 3.3.22 && \
    update_rubygems
	

# We usually run this every time we add a new dependency
RUN gem install bundler -v 2.4.22
RUN gem install jekyll -v 3.9.3
RUN bundle install


EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--safe"]
