FROM ruby:2.7.4

WORKDIR /myapp
COPY . /myapp

# We usually run this every time we add a new dependency
RUN gem install bundler
RUN gem install jekyll -v 3.9.3
RUN bundle install


EXPOSE 4000

CMD bundle exec jekyll s --host 0.0.0.0 --safe
