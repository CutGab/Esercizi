const rootElement = document.querySelector("#root");

const root = ReactDOM.createRoot(rootElement);

const App = (props) => {
    return (
        <main className="main">
            <h1> Primo componente </h1>
             {props.children}
        </main>
        
    )
}

const List = () => {
    return(
        <ul>
            <li> JAVASCRIPT</li>
            <li> PHP </li>
            <li> PYTHON </li>
        </ul>
    )
}

root.render(
    <>
        <App>
            <h2> Lista dev </h2>
            <List></List>   
        </App>    
    </>
)