import React ,{Component} from 'react';
import Button from "@material-ui/core/Button";
import ButtonGroup from "@material-ui/core/ButtonGroup";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import {Link} from"react-router-dom";
import Tooltip from "@material-ui/core/Tooltip"
import { withStyles, makeStyles } from '@material-ui/core/styles';
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";

const HtmlTooltip = withStyles((theme) => ({
    tooltip: {
        backgroundColor: '#212121',
        color: '#4dd0e1',
      maxWidth: 220,
      fontSize: theme.typography.pxToRem(12),
      border: '1px solid #dadde9',
      textAlign:'center',
    },
  }))(Tooltip);

export default class CreatePalacePage extends Component { 
    constructor(props) {
        super(props);
    }
    render(){
        return(
        <Grid container spacing = {1}>
            <Grid item xs={12} align="center">
                <Typography component = "h4" variant= "h4">
                    Choose your preferred version
                    <br/>
                    <br/>
                </Typography>
            </Grid>
            
            <Grid item xs={12} align="center">    
            <Button color = "primary" variant ="contained"  to="/v1" component={Link}>Version 1</Button>
            </Grid>
            <Grid item xs={12} align="center">    
            <Button color = "primary" variant ="contained"  to="/v2" component={Link}>Version 2</Button>
            </Grid>
            <Grid item xs={12} align="center">    
            <Button color = "primary" variant ="contained"  to="/v3" component={Link}>Version 3</Button>
            <br/>
            <br/>
            <br/>
            </Grid>
            
            <Grid item xs={12} align="center">    
            <Button  color = "secondary"  variant ="outlined"  to="/versions" component={Link}>More about the versions</Button>
            

           
            </Grid>    
            <Grid item xs={12} align="center">
                <Button color = "secondary" variant ="contained"  to="/" component={Link}>Home</Button>
            </Grid>
        </Grid>
        ); 
    }
}