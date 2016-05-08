var Connection = function () {
    Connection.prototype.startGame()
}

Connection.prototype.convertAction = function(action){
    return 63 - parseInt(action);
}

Connection.prototype.startGame = function(){
    $.ajax({
      type: "GET",
      url: "/start",
      success: function(){
      },
      dataType: 'application/json'
    });    
    
}

Connection.prototype.nextAction = function(board,previousAction,callback){

    var bits = board.getBitStrings();
    var p1 = bits[0];
    var p2 = bits[1];
    var previousAction = this.convertAction(previousAction);
    var data = JSON.stringify({p1:p1,p2:p2,action:previousAction})
    $.ajax({
      type: "POST",
      url: "/ai",
      data: data,
      context: this,
      contentType: 'application/json',
      success: function(result){
          action = this.convertAction(result.next)
          callback(action)
      },
      error:function(){
          alert("hoge")
      },
      dataType:'json'
    });
};
