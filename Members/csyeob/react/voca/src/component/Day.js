import { useParams } from "react-router-dom";
import Word from "./Word";
import { useEffect, useState } from 'react';
import useFetch from './../hooks/useFetch';
export default function Day(){
    //dummy.words   
    const {day} = useParams();
    //const wordList = dummy.words.filter(word=>(word.day === Number(day)))
    const words = useFetch(`http://localhost:3002/words?day=${day}`);
    // const [words, setWords] = useState([]);

    // useEffect(() =>{
    //     fetch(`http://localhost:3002/words?day=${day}`)
    //     .then(res => {
    //         return res.json();
    //       })
    //       .then(data => {
    //         setWords(data);
    //       });
    //   }, [day]);


    const a  = useParams();
    console.log(a);
    return<>
    <h2>Day {day}</h2>
    <table>
        <tbody>
            {words.map(word =>(
                <Word word={word} key = {word.id}/>
            ))}
        </tbody>
    </table>
    </>;
}
