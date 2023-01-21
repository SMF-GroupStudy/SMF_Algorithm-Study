const express = require('express')
const app = express()

app.use(express.json()) // for parsing application/json
app.use(express.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded

let id = 2;
const todoList = [{
    id: 1,
    text: '할일 1',
    done: false,
}];

app.get('/', function (req, res) {
  res.send('Hello World')
});

app.get('/api/todo',(req,res)=>{
    res.json(todoList);
    //json형태로 보냄.
});

app.post('/api/todo', (req, res)=>{
    const {text, done} = req.body;
    //body에서 꺼내쓸려면 body parser가 필요함.
    todoList.push({
        id:id++,
        text,
        done,
    });
    return res.send('success');
});

app.listen(3000, () =>{
    console.log('server start!');
});