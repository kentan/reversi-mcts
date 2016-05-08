
var BoardView = React.createClass({displayName: 'BoardView',
  getInitialState: function () {
    return {board: new Board,connection:new Connection};
  },
  restartGame: function () {
    this.setState(this.getInitialState());
  }, 
                                
  putOpponentTile : function(action){
      var board = this.state.board.putTile(action)
      this.setState({board : board});
  },
                                   
  handleOnClick: function(event){
      if(event.target.attributes.id == undefined) return ;
      var id = event.target.attributes.id.value;
      var board = this.state.board.putTile(id)
      this.state.connection.nextAction(board,id,this.putOpponentTile)
      this.setState({board : board});
  },

  render: function () {
    var index = 0;
    var key = 0;
    var cells = this.state.board.cells.map(function (row) {
      return React.DOM.div({key:key++}, row.map(function (tile) {return React.DOM.span({className: "cell",key:key++,id:index++}, "")}))
    });
    var tiles = this.state.board.cells.map(function (row) {
        return React.DOM.div({key:key++}, row.filter(function(tile){
            return tile.value != 0;
        }).map(function(tile){
            return <TileView tile={tile} key={key++}/>;
        }));
    });
                             
    
    return (
        React.DOM.div({className:"main"},
             React.DOM.div({className: "board", tabIndex:"2",onClick:this.handleOnClick},
             cells,
             tiles),
             <InfoView playerId={this.state.board.playerId} passed={this.state.board.pass}/>
         ));
  }
});


var TileView = React.createClass({displayName: 'TileView',

  render: function () {
      var tile = this.props.tile;
      var classes = "tile ";
      var tileColor = tile.value == 1 ? 'blackTile' : 'whiteTile';
      classes += tileColor + " ";

      classes += "position_" + tile.row + "_" + tile.column;

      return (
        React.DOM.span({className: classes}, "")
      );
  }
});

var InfoView = React.createClass({displayName: 'InfoView',
  render: function () {
      var playerId = this.props.playerId;
      var tileColor = playerId == 1 ? 'blackTile' : 'whiteTile';
      var classes = tileColor;
      var passedMessage = this.props.passed ? "PASSED" : "";
      return (
          React.DOM.div({className:"info"},
            React.DOM.p(null,"You are "),
            React.DOM.div({className: classes}, ""),
            React.DOM.p(null,passedMessage)
          )
       );
  }                         
});

ReactDOM.render(<BoardView/>, document.getElementById('universe'));
