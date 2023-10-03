#!/usr/bin/env ruby
# Expected script output: [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
