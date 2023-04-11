const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const MONGO_URI = 'mongorestore --uri="<YOUR_CONNECTION_STRING'

mongoose.connect(MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})

//define and export schema
const userSchema = new Schema({
  username: {type: String, required: true, unique: true},
  email: {type: String, required: true, unique: true},
  level: {type: Number, required: true},
  lastLogin: {type: Date, required: false},
  user_id: {
    type: Schema.Types.ObjectId,
    ref: 'user'
  }
});

module.exports = mongoose.model('User', UserSchema);