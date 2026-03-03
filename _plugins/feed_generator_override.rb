# frozen_string_literal: true

# Overriding feed generator to speed up build times
# From: https://github.com/jekyll/minima/issues/562


module JekyllFeed
  class Generator < Jekyll::Generator
    safe true
    priority :lowest

    # Main plugin action, called by Jekyll-core
    def generate(_site)
    end
  end
end
