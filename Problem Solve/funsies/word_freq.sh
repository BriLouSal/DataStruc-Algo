# Read from the file words.txt and output the word frequency list to stdout.
# We can use the cat command and read the context of it
cat words.txt | tr -s ' ' '\n' | sort | uniq -c |sort -r | awk '{print $2, $1}'
