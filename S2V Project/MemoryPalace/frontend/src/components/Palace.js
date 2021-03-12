import React, {Component} from 'react';
import {ButtonGroup,Button,Grid,Typography} from "@material-ui/core";
import {Link} from"react-router-dom";

export default class Palace extends Component { 
    defaultTheme = "";  
    defaultVersion = 0;
    defaultPW = 0;
    defaultSLW = 0;
    defaultFLW = 0;
    defaultPWSW = 0;

    constructor(props) {
        super(props);
        this.state={
            theme:this.defaultTheme,
            version: this.defaultVersion,
            phonetic_weight: this.defaultPW,
            second_letter_weight: this.defaultSLW,
            first_letter_weight: this.defaultFLW,
            previous_word_weight:this.defaultPWSW
        }
        this.user = this.props.match.params.user;
        this.getPalaceDetails();
    }

    
  getPalaceDetails() {
    fetch("/api/get-palace" + "?user=" + this.user)
      .then((response) => response.json())
      .then((data) => {
        this.setState({
            theme:data.theme,
            version: data.version,
            phonetic_weight: data.phonetic_weight,
            previous_word_weight: data.previous_word_weight,
            first_letter_weight: data.first_letter_weight,
            second_letter_weight: data.second_letter_weight,
            words_to_remember: data.words_to_remember,
            trigger_words: data.trigger_words
        });
      });
  }



    render(){
        return(
            <Grid container spacing ={1}>
                <Grid item xs={12} align="center">
                    <Typography variant = "h3" compact="h3">
                        Your trigger words:
                    </Typography>
                    <Typography variant = "h4" compact="h4">
                        {this.state.trigger_words}
                    </Typography>
                </Grid>
                <Grid item xs ={12}align="center">
                <Typography variant = "h6" compact="h6">
                    Your settings:
                </Typography>
                <Typography variant = "subtitle1" compact="subtitle1">
                    Words to remember:  {this.state.words_to_remember}
                </Typography>
                <Typography variant = "subtitle1" compact="subtitle1">
                    Theme: {this.state.theme}
                </Typography>
                <Typography variant = "subtitle1" compact="subtitle1">
                    Version: {this.state.version}
                </Typography>
                <Typography variant = "subtitle1" compact="subtitle1">
                    Phonetic Weight:  {this.state.phonetic_weight}
                </Typography>
                <Typography variant = "subtitle1" compact="subtitle1">
                    Preceeding Word Weight:  {this.state.second_letter_weight}
                </Typography>
                <Typography variant = "subtitle1" compact="subtitle1">
                    First Letter Weight:  {this.state.second_letter_weight}
                </Typography>
                <Typography variant = "subtitle1" compact="subtitle1">
                    Secound Letter Weight:  {this.state.second_letter_weight}
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
            <Button color = "secondary" variant ="contained"  to="/create" component={Link}>Create another palace</Button>
        </Grid>
    </Grid>
        );
    }
}