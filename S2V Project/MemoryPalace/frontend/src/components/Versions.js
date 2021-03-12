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
                    <Typography variant = "h5" compact="h5">
                        Version 1
                    </Typography>
                    <Typography variant = "subtitle1" compact="subtitle1">
                        Version 1 requires a theme. The list of "trigger words" it produces will all follow as closely as possible to this theme. In this version every "trigger word" will have the same first letter its corresponding "word to remember". The user can  choose the thme, the phonetic weight (how important it is for each "trigger word" to rhyme with its "word to remember") and the secound letter weight (how important it is for the second letter of each "trigger word" to be the same as the second letter for its corresponding "word to remember").
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <Typography variant = "h5" compact="h5">
                        
                        Version 2
                    </Typography>
                    <Typography variant = "subtitle1" compact="subtitle1">
                        Version 2 removes the requirement of a theme and now allows the user to decide how important it is for each "trigger word" to have the samne starting letter as its corresponding "word to remember". It still consioders the phonetic and second letter weights the same as Version 1 , but now it also consider how similar each word in the "trigger list" is to its predecessor, therefore allowing the output to find a theme of its own. 
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <Typography variant = "h5" compact="h5">
                        
                        Version 3
                    </Typography>
                    <Typography variant = "subtitle1" compact="subtitle1">
                        Version 3 is identical to Version 2 apart from how it calculates each "trigger words" similarity to its predecessor. In this version the weight the user inputs determines how dissimilar the word should be to its predecessor to allow for a more unusual , and hopefully more memorable, output.
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                <Button color = "secondary" variant ="contained"  to="/create" component={Link}>Go Back</Button>
            </Grid>
            </Grid>
        );
    }
}