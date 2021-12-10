const express = require('express');
const expressLayouts = require('express-ejs-layouts');

const app = express();
const post = process.env.PORT || 3000;

require('dotenv').config();

app.use(express.urlencoded( { extended: true } ));
app.use(express.static('public'));
app.use(expressLayouts);

app.set('layout', './layouts/main');

const routes = require('./server/route/recipeRoutes.js')
app.use('/', routes);

app.listen(port, ()=> console.log(`Listening to port ${port}`));

