echo random process
date &

id=$!
echo ""
echo "id: "
echo $id

echo ""
echo "job :"
jobs


echo ""
echo "killing $id"
kill -9 $id

echo ""
echo "curernt status: "
jobs
