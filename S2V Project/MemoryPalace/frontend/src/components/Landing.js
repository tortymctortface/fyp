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
                    <ButtonGroup disableElevation variant="contained">
                        <Button color="secondary" to='/create' component={Link}>
                            Build a Palace
                        </Button>
                        <Button color="secondary" variant="outlined" to='/about' component={Link}>
                            About us
                        </Button>
                    </ButtonGroup>
                </Grid>
            </Grid>
        );
    }
}