###
#   
#  Arrange integer arguments in ascending order
#
###



result = []
ARGV.each do |arg|
    # if not an integer skip
    next if arg !~ /^-?[0-9]+$/

    # convert to an integer
    i_arg = arg.to_i
    
   # Insert the result at the apropriate position
    is_inserted = false
    i = 0
    l = result.size
    while !is_inserted && i < l do
        if result[i] < i_arg
            i += 1
        else
            result.insert(i, i_arg)
            is_inserted = true
            break
        end
    end
    result << i_arg if !is_inserted
end

puts result