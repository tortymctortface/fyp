import React ,{Component} from 'react';
import CreatePalacePage from "./CreatePalacePage";
import Palace from "./Palace";
import Versions from "./Versions"
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";
import Landing from './Landing';
import AboutUs from './AboutUs';
import AboutMemoryPalace from './AboutMemoryPalace';
import V1 from "./V1"
import V2 from "./V2"
import V3 from "./V3"

export default class Routes extends Component {
    constructor(props) {
        super(props);
    }

    render(){
        return (
            <Router>
                <Switch>
                    <Route exact path= '/' component = {Landing}/>
                    <Route path= '/create' component = {CreatePalacePage} />
                    <Route path= '/palace/:user' component = {Palace} />
                    <Route path= '/versions' component = {Versions} />
                    <Route path= '/about' component = {AboutUs} />
                    <Route path= '/about-palace' component = {AboutMemoryPalace} />
                    <Route path='/V1' component = {V1}/>
                    <Route path='/V2' component = {V2}/>
                    <Route path='/V3' component = {V3}/>
                </Switch>
            </Router>
        );
    }
}