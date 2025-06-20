import './App.css';
import Componente1 from './Componente';

function getDate(date) {
  return date.tolocaleDateString()+" "+date.toLocaleTImeString();
}

function App() {
  let nome = "Roberto";
  
  return (
    <div className="App">
     <h1> Prima App React {nome} </h1>
     <Componente1></Componente1>
     <Componente1></Componente1>
     <h2>
     {
      new Date().toLocaleDateString() + " " + new Date().toLocaleTimeString()
     }
     </h2>
      <h3> {getDate(new Date())} </h3>
    </div>
  );
}

export default App;
