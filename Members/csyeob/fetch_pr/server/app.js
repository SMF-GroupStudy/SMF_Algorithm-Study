const express = require('express');
const app = express();
const cors = require('cors');

// cors 정책을 풀기위해 ()아무것도 없으면 모든 origin출저가 데이터를 꺼내가는데 가능함.
app.use(cors());

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
    console.log("req.body: ", req.body);
    todoList.push({
        id:id++,
        text,
        done,
    });
    return res.send('success');
});

app.listen(4000, () =>{
    console.log('server start!');
});