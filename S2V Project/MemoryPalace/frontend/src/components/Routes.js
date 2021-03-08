import React ,{Component} from 'react';
import CreatePalacePage from "./CreatePalacePage";
import Palace from "./Palace";
import Versions from "./Versions"
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";
import Landing from './Landing';
import AboutUs from './AboutUs';

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
                </Switch>
            </Router>
        );
    }
}