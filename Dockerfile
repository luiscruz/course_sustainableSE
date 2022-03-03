FROM ruby:3

WORKDIR /myapp
COPY . /myapp

# We usually run this every time we add a new dependency
RUN gem install bundler
RUN gem install jekyll
RUN bundle install


EXPOSE 4000

CMD bundle exec jekyll s --safe
