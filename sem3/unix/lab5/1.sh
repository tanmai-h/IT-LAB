d=$(date +'%H')
m=$(date +'%M')

if ((d>0 && d<12 ))
then
  echo Good Morning
elif ((d >= 12 && d<18))
then
  echo Good Afternoon
elif ((d >= 18 && d<20))
then
  echo Good Evening
elif ((d >= 20 || d <3))
then
  echo Good Night
fi



