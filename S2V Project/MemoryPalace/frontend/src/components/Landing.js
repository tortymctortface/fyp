import React ,{Component} from 'react';
import {ButtonGroup,Button,Grid,Typography} from "@material-ui/core";
import  {Link} from "react-router-dom";

export default class Landing extends Component {
    constructor(props) {
        super(props);
    }

    render(){
        return (
            <Grid container spacing={3}>
                <Grid item xs={12} align="center">
                    <Typography variant = "h3" compact="h3">
                        Memory Palace Builder
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    
                        <Button color="primary" variant="contained" to='/create' component={Link}>
                            Build a Palace
                        </Button>
                </Grid>        
                <Grid item xs={12} align="center">
                        <Button color="primary"  to='/about-palace' component={Link}>
                            What's a Memory Palace?
                        </Button>
                
                </Grid>
                <Grid item xs={12} align="center">
                        <Button color="secondary"  to='/about' component={Link}>
                            About us
                        </Button>
                </Grid>
            </Grid>
        );
    }
}