# Learning about Terminal form the course ADVANCED COMMAND LINE TECHNIQUES by TUTS+ #

### awk - programming language ###
awk is pattern scanning and processing language

 
ls -l | awk '{ print $5  }'
ls -l | awk '{ print $2, '\t', $1  }'
awk 'BEGIN { print "Last \t Job"  } { print $2, '\t', $4  }'
cat test.txt | awk '{print NR, NF, $0 }'
ls -l | awk '{ if ( NF >= 9  ) { print $9  }  }'


