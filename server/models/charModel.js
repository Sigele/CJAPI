const mongoose = require('mongoose');
const Schema = mongoose.Schema;

//connect mongoose schema to DB
const MONGO_URI = 'mongorestore --uri="mongodb+srv://Sigele:65wEJ5Bi746QzZG@cluster1.yx0hcby.mongodb.net/?retryWrites=true&w=majority'



mongoose.connect(MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})

//define and export schema
const charSchema = new Schema({
  character: {type: String, required: true, unique: true},
  qwerty: {type: String, required: true},
  radicals: {type: String, required: true},
  link: {type: String, required: true, unique: true},
  level: {type: Number, required: true, unique: false},
  doubled: {type: Boolean, required: true, unique: false},
  char_id: {
    type: Schema.Types.ObjectId,
    ref: 'character'
  }
});

module.exports = mongoose.model('Char', charSchema);