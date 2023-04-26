import { json } from 'body-parser';
import React, { Component } from 'react';

class User extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currUser: null,
      signedIn: false,
      userScore: 0,
      userLevel: 1
    }

    this.getUser = this.getUser.bind(this);

    this.getScore = this.getScore.bind(this)

  }
  componentDidMount() {

  }

  render() {
    <div>hey hey it's the user Component!</div>
  }
}

export default User;