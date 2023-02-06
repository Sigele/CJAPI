const mongoose = require('mongoose');
const Schema = mongoose.Schema;


/*example entry:
 entrySC: '已经',
 entryTC: '已經',
 jyutping: 'ji5 ging1',
 pinyin: 'yǐjīng',
 input: [S, U, V, F, M, V, M],
 radicals: ['尸','山','女','火','一','女','一'],
 audio: {'somefilename.mp3'}


since this API is focused on typed input, I'm not making pronunciation required. It is a good idea to encourage users to add either jyutping or pinyin. No plans to accept Yale or Zhuyin/other input methods for now.
*/ 
const entrySchema = new Schema({
  entrySC: {type: String, required: true, unique: true},
  entryTC: {type: String, required: true, unique: true},
  jyutping: {type: String},
  pinyin: {type: String},
  input: {type: Array, required: true},
  radicals: {type: Array, required: true},
  audio: {type: String}

})

module.exports = mongoose.model('Entry', entrySchema);