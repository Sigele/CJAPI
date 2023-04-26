import React, { useState } from 'react';
import { render } from 'react-dom';


 class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      user: null,
      testCards: [],
      fetchedCards: false,

    }

  }

  componentDidMount() {
    //fetch stuff
  }

  render() {
    return(
      <div> HI </div>
    )
  };
 };

 render(<App/>, document.getElementById('root'))