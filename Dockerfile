FROM ruby:2.7.7

WORKDIR /myapp
COPY . /myapp

# We usually run this every time we add a new dependency
RUN gem install bundler
RUN gem update --system
RUN gem install sass-embedded -v 1.58.3
RUN gem install jekyll
RUN bundle install


EXPOSE 4000

CMD bundle exec jekyll s --host 0.0.0.0 --safe
