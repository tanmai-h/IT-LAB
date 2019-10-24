var bodyParser = require('body-parser');

var controller = function(app){
    app.use(bodyParser.urlencoded({extended: true}));
    app.use(bodyParser.json());
    
    app.get('/',function(req,res){
        console.log(req.url);        
        res.render('index.ejs');
    });

    app.post('/', function(req, res) {
        console.log(req.body);
        res.render('result.ejs',{data:req.body});
    });
    app.use(function(req, res) {
        res.render("404.ejs");
    });
}

module.exports = controller;