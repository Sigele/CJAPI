require('dotenv').config()

const express = require('express');
const path = require('path');
const app = express();
const mongoose = require('mongoose')
const PORT = 3000;
const { MongoClient, ServerApiVersion } = require('mongodb');
const uri = "mongodb+srv://Sigele:65wEJ5Bi746QzZG@cluster1.yx0hcby.mongodb.net/?retryWrites=true&w=majority";
//add controllers!

mongoose.connect(process.env.DATABASE_URL, {
  useNewUrlParser: true
})

const db = mongoose.connection
db.on('error', (error) => console.error(error))
db.once('open', () => console.log('connected to database'))

app.use(express.json());

//serve static files


//delete entries
//return entry or entries

//add entries (scraper)




app.get('/',(req,res) => {
  return res.sendFile(path.resolve('client', 'index.html'));
});

//global error handling
app.use((err, req, res, next) => {
  const defaultErr = {
    log: 'Express error handler caught an unknown middleware error',
    status: 400,
    message: {
      err: 'An error occurred :('
    },
  };

  const errObj = Object.assign(defaultErr, err);
  console.log(errObj.log);
  res.status(errObj.status).send(JSON.stringify(errObj.message));
});

//listen at assigned port
app.listen(PORT, () => {
  console.log(`Listening on Port ${PORT}`);
});

module.exports = app;