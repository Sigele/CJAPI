const express = require('express');
const path = require('path');
const app = express();
const PORT = 3333;

//add controllers!

app.use(express.json());

//serve static files


//delete entries
//return entry or entries

//add entries (scraper)
app.post()

app.delete()

app.get()

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