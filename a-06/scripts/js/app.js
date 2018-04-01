// init the node reference path
var buttons = new Firebase('https://ms-iot.firebaseio.com/boards');

// refresh the list in HTML
function refreshList(children) {
    var sections = '';
    for (var i = 0; i < children.length; i++) {
        sections += '<li>' + children[i].key + ': ' + children[i].state + '</li>';
    };
    document.getElementById('buttons').innerHTML = sections;
};

// listen for value changes on children
buttons.on("value", function(snapshot) {
    var data = snapshot.val();
    var children = [];
    for (var key in data) {
      state = data[key];
      if (key.trim().length > 0) {
          children.push({
              state: state,
              key: key
          })
      }
    }

    refreshList(children);
});
