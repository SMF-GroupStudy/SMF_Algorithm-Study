import dummy from "../db/data.json";
import { useParams } from "react-router-dom";
export default function Day(){
    //dummy.words   
    const {day} = useParams();
    const wordList = dummy.words.filter(word=>(word.day === Number(day)))
    
    const a  = useParams();
    console.log(a);
    return<>
    <h2>Day {day}</h2>
    <table>
        <tbody>
            {wordList.map(word =>(
                <tr key ={word.id}>
                    <td><input type="checkbox"></input></td>
                    <td>{word.eng}</td>
                    <td>{word.kor}</td>
                    <td>
                        <button>뜻보기</button>
                        <button class ="btn_del">삭제</button>
                    </td>
                </tr>
            ))}
        </tbody>
    </table>
    </>;
}
