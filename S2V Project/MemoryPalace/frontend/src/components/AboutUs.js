import React ,{Component} from 'react';
import {ButtonGroup,Button,Grid,Typography} from "@material-ui/core";
import  {Link} from "react-router-dom";

export default class AboutUs extends Component {
    constructor(props) {
        super(props);
    }

    render(){
        return (
            <Grid container spacing={3}>
                <Grid item xs={12} align="center">
                    <Typography variant = "h4" compact="h4">
                        About us
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                <Typography variant = "subtitle1" compact="h3">
                        This web application was built as part of a final year project.
                    </Typography>
                    <Typography variant = "subtitle1" compact="h3">
                       See <a href="https://github.com/tortymctortface/fyp">here</a> for the projects code
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                <Button color = "secondary" variant ="contained"  to="/" component={Link}>Go Back</Button>
            </Grid>
            </Grid>
        );
    }
}