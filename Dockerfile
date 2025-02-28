FROM ruby:3.1

WORKDIR /myapp
COPY . /myapp

# Install bundler and required gems using the Gemfile
RUN gem install bundler -v 2.4.22
RUN bundle install

EXPOSE 4000

CMD bundle exec jekyll serve --host 0.0.0.0
