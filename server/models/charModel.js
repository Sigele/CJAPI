const mongoose = require('mongoose');
const Schema = mongoose.Schema;

//connect mongoose schema to DB
const MONGO_URI = 'mongorestore --uri="<YOUR_CONNECTION_STRING'

mongoose.connect(MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})

//define and export schema
const charSchema = new Schema({
  entry: {type: String, required: true, unique: true},
  input: {type: String, required: true},
  radicals: {type: String, required: true},
  link: {type: String, required: true, unique: true},
  char_id: {
    type: Schema.Types.ObjectId,
    ref: 'character'
  }
});

module.exports = mongoose.model('Char', charSchema);