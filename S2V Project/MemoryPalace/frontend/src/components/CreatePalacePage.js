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
    defaultTheme = "food";  
    defaultVersion = 2;
    defaultPW = 0.2;
    defaultSLW = 0.1;
   
    constructor(props) {
        super(props);
        this.state={
            theme:this.defaultTheme,
            version: this.defaultVersion,
            phonetic_weight: this.defaultPW,
            second_letter_weight: this.defaultSLW,
            user : null
        }

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleThemeChange = this.handleThemeChange.bind(this);
        this.handleVersionChange = this.handleVersionChange.bind(this);
        this.handlePWChange = this.handlePWChange.bind(this);
        this.handleSLWChange = this.handleSLWChange.bind(this);
        this.handleWordsToRememberChange = this.handleWordsToRememberChange.bind(this);
        this.user = this.props.match.params.user;
        
    }

    handleThemeChange(e){
        this.setState({
            theme: e.target.value
        });
    }

    handleVersionChange(e){
        this.setState({
           version: e.target.value
        })
    }

    handlePWChange(e){
        this.setState({
            phonetic_weight: e.target.value
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
                theme: this.state.theme,
                version: this.state.version,
                phonetic_weight: this.state.phonetic_weight,
                second_letter_weight: this.state.second_letter_weight,
                words_to_remember: this.state.words_to_remember
            })
        };
        fetch("/api/create-palace", requestOptions).then((response)=>
            response.json()
        ).then((data) => this.props.history.push("/palace/" + data.user));
    }
    async componentDidMount(){
        fetch("/api/recent-palace")
        .then((response)=>response.json())
        .then((data)=>{
            this.setState({
                user: data.user
            })
        });
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
                <FormControl>
                    <TextField 
                        required = {true}
                        type = "number"
                        onChange={this.handleVersionChange}
                        defaultValue = {this.defaultVersion}
                        inputProps={{
                            min:1,
                            max:3,
                            style:{textAlign: "center"},
                        }}
                    />
                    <FormHelperText>
                        <div align="center">Version</div>
                    </FormHelperText>
                    <HtmlTooltip
                        title={
                            <React.Fragment>
                            <Typography color="inherit">The version you chose will affect the requirements for your palace as well as the style of it's output</Typography>
                        </React.Fragment>
                        }
                        >
                        <Button>?</Button>
                    </HtmlTooltip>
                </FormControl>
            </Grid>
            <Grid item  xs={12} align="center">
                <FormControl component = "fieldset">
                <TextField 
                        required = {true}
                        type = "string"
                        onChange={this.handleThemeChange}
                        defaultValue = {this.defaultTheme}
                        inputProps={{
                            style:{textAlign: "center"},
                        }}
                    />
                    <FormHelperText>
                        <div align='center'>
                           Theme
                        </div>
                    </FormHelperText>
                    <HtmlTooltip
                        title={
                            <React.Fragment>
                            <Typography color="inherit">Enter a one word noun such as food, art or animal. This will be the overall theme of your Memory Palace</Typography>
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
                            max:0.99,
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
                        onChange={this.handleSLWChange}
                        defaultValue = {this.defaultSLW}
                        inputProps={{
                            min:0.00,
                            max:0.99,
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
                    >Build</Button>
            </Grid>       
            <Grid item xs={12} align="center">
            <ButtonGroup disableElevation variant="outlined">
            <Button 
                    color = "primary" 
                    to={`/palace/${this.state.user}`}
                    component={Link}
                    >My most recent Palace</Button>
                    
                <Button color = "secondary"   to="/versions" component={Link}>More about the versions</Button>
            </ButtonGroup>
            </Grid>
            <Grid item xs={12} align="center">
                <Button color = "secondary" variant ="contained"  to="/" component={Link}>Go Back</Button>
            </Grid>
        </Grid>
        ); 
    }
}