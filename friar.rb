
$stdin.each do |line|
  line.gsub(/ +/, ' ')
  debtor, rest = line.split(' owes ', 2)
  lender, rest = rest.split(' ', 2)
  amount = rest.split.first.to_f

  puts "#{debtor} owes #{lender} #{amount}"
end
