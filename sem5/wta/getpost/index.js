var express = require('express');
var app = express();
app.set('view-engine','ejs');
app.use(express.static('public'));
var controller = require('./controllers/controller.js');

controller(app);


app.listen(3000,function(){
    console.log("Listening to port 3000");
});