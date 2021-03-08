import React ,{Component} from 'react';
import {ButtonGroup,Button,Grid,Typography} from "@material-ui/core";
import  {Link} from "react-router-dom";

export default class Versions extends Component {
    constructor(props) {
        super(props);
    }

    render(){
        return (
            <Grid container spacing={3}>
                <Grid item xs={12} align="center">
                    <Typography variant = "h3" compact="h3">
                        Choose one of three versions
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <Typography variant = "h6" compact="h6">
                        Version selection has been temporarily removed. Version 1, 2 and 3 will all accept a list of single words separated by a comma. 
                    </Typography>
                    <Typography variant = "h6" compact="h6">
                        The list returned currently requires a theme and will only choose trigger words that start with the same letter as their corresponding word to remember
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                <Button color = "secondary" variant ="contained"  to="/create" component={Link}>Go Back</Button>
            </Grid>
            </Grid>
        );
    }
}