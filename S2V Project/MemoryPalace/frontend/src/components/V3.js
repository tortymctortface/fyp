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

export default class V3 extends Component {
    defaultVersion = 3;
    defaultPWSW = 0;
    defaultPW = 0;
    defaultFLW=0;
    defaultSLW=0;
   
    constructor(props) {
        super(props);
        this.state={
            previous_word_weight:this.defaultPWSW,
            version: this.defaultVersion,
            phonetic_weight: this.defaultPW,
            first_letter_weight: this.defaultFLW,
            second_letter_weight: this.defaultSLW,
         
        }

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handlePWSWChange = this.handlePWSWChange.bind(this);
        this.handlePWChange = this.handlePWChange.bind(this);
        this.handleFLWChange = this.handleFLWChange.bind(this);
        this.handleSLWChange = this.handleSLWChange.bind(this);
        this.handleWordsToRememberChange = this.handleWordsToRememberChange.bind(this);
       
        
    }

    handlePWSWChange(e){
        this.setState({
            previous_word_weight: e.target.value
        });
    }

    handlePWChange(e){
        this.setState({
            phonetic_weight: e.target.value
        })
    }

    handleFLWChange(e){
        this.setState({
            first_letter_weight: e.target.value
        })
    }

    handleSLWChange(e){
        this.setState({
            second_letter_weight: e.target.value
        })
    }
    handleWordsToRememberChange(e){
        this.setState({
            words_to_remember: e.target.value
        });
    }

    handleSubmit(){
        const requestOptions = {
            method:'POST',
            headers: {'Content-Type' : 'application/json'},
            body: JSON.stringify({
                previous_word_weight: this.state.previous_word_weight,
                version: this.state.version,
                phonetic_weight: this.state.phonetic_weight,
                first_letter_weight:this.state.first_letter_weight,
                second_letter_weight: this.state.second_letter_weight,
                words_to_remember: this.state.words_to_remember
            })
        };
        fetch("/api/create-palace", requestOptions).then((response)=>
            response.json()
        ).then((data) => this.props.history.push("/palace/" + data.user));
    }

    render(){
        return(
        <Grid container spacing = {1}>
            <Grid item xs={12} align="center">
                <Typography component = "h4" variant= "h4">
                    Create your Memory Palace
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <Typography component = "h5" variant= "h5">
                   Version 3
                    <br/>
                    <br/>
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <TextField 
                        required = {true}
                        type = "decimal"
                        defaultValue = {this.defaultPWSW}
                        onChange={this.handlePWSWChange}
                        inputProps={{
                            min:0.00,
                            max:1.00,
                            style:{textAlign: "center"},
                        }}
                    />
                    <FormHelperText>
                        <div align="center">Dissimilarity to preceeding word weight</div>
                    </FormHelperText>
                    <HtmlTooltip
                        title={
                            <React.Fragment>
                            <Typography color="inherit">Enter a value between 0.00 and 0.99. This will determine how dissimilar each trigger word should be to the chosen trigger word for the previous word to remember.</Typography>
                        </React.Fragment>
                        }
                        >
                        <Button>?</Button>
                    </HtmlTooltip>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <TextField 
                        required = {true}
                        type = "decimal"
                        onChange={this.handlePWChange}
                        defaultValue = {this.defaultPW}
                        inputProps={{
                            min:0.00,
                            max:1.00,
                            style:{textAlign: "center"},
                        }}
                    />
                    <FormHelperText>
                        <div align="center">Phonetic Weight</div>
                    </FormHelperText>
                    <HtmlTooltip
                        title={
                            <React.Fragment>
                            <Typography color="inherit">Enter a value between 0.00 and 0.99. This will determine how important the phonetic similarity between each 'word to remember' it's corresponding chosen 'trigger word' is.</Typography>
                        </React.Fragment>
                        }
                        >
                        <Button>?</Button>
                    </HtmlTooltip>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <TextField 
                        required = {true}
                        type = "decimal"
                        onChange={this.handleFLWChange}
                        defaultValue = {this.defaultFLW}
                        inputProps={{
                            min:0.00,
                            max:1.00,
                            style:{textAlign: "center"},
                        }}
                    />
                    <FormHelperText>
                        <div align="center">First letter weight</div>
                    </FormHelperText>
                    <HtmlTooltip
                        title={
                            <React.Fragment>
                            <Typography color="inherit">Enter a value between 0.00 and 0.99. This will determine how important it is for each 'word to remember' to have the same first letter as it's corresponding 'trigger word' is.</Typography>
                        </React.Fragment>
                        }
                        >
                        <Button>?</Button>
                    </HtmlTooltip>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <TextField 
                        required = {true}
                        type = "decimal"
                        onChange={this.handleSLWChange}
                        defaultValue = {this.defaultSLW}
                        inputProps={{
                            min:0.00,
                            max:1.00,
                            style:{textAlign: "center"},
                        }}
                    />
                    <FormHelperText>
                        <div align="center">Second letter weight</div>
                    </FormHelperText>
                    <HtmlTooltip
                        title={
                            <React.Fragment>
                            <Typography color="inherit">Enter a value between 0.00 and 0.99. This will determine how important it is for each 'word to remember' to have the same second letter as it's corresponding 'trigger word' is.</Typography>
                        </React.Fragment>
                        }
                        >
                        <Button>?</Button>
                    </HtmlTooltip>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
               <FormControl component = "fieldset">
                    <TextField 
                        required = {true}
                        type = "string"
                        id="outlined-basic" 
                        variant="outlined"
                        onChange={this.handleWordsToRememberChange}
                        multiline
                        rows={2}
                        rowsMax={4}
                        inputProps={{
                            style:{textAlign: "center"},
                        }}
                    />
                    <FormHelperText>
                        <div align='center'>
                           Words to remember
                        </div>
                    </FormHelperText>
                    <HtmlTooltip
                        title={
                            <React.Fragment>
                            <Typography color="inherit">pleae</Typography>
                        </React.Fragment>
                        }
                        >
                        <Button>?</Button>
                    </HtmlTooltip>
                </FormControl>      
            </Grid>
            <Grid item xs={12} align="center">
            
                <Button 
                    color = "primary" 
                    variant ="contained"
                    onClick={this.handleSubmit}  
                    >Build </Button>
            </Grid>       
            
            <Grid item xs={12} align="center">
                <Button color = "secondary" variant ="contained" to="/create" component={Link}>Go Back</Button>
            </Grid>
        </Grid>
        ); 
    }
}