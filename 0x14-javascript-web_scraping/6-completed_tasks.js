#!/usr/bin/node

/* Fetch completed todos & display user id */
const req = require('request');
const args = process.argv;
const completedTodos = {};
req(args[2], function (err, res, body) {
  if (err) throw err;
  else {
    const reply = JSON.parse(body);
    reply.forEach((todo) => {
      if (todo.completed) {
        // If userId has not done todo just add 1
        if (!completedTodos[todo.userId]) {
          completedTodos[todo.userId] = 1;
        } else {
        // If userId has done a todo just add +1
          completedTodos[todo.userId] += 1;
        }
      }
    });
  }
  console.log(completedTodos);
});
