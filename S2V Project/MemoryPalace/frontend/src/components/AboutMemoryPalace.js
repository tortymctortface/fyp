import React ,{Component} from 'react';
import {ButtonGroup,Button,Grid,Typography} from "@material-ui/core";
import  {Link} from "react-router-dom";
import AboutUs from './AboutUs';

export default class AboutMemoryPalace extends Component {
    constructor(props) {
        super(props);
        
    }
    render(){
        return (
        <div
            class="ScrollStyle">
            <Grid container spacing={3}>
                <Grid item xs={12} align="center">
                    <Typography variant = "h3" compact="h3">
                        Memory Palace's
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                <Typography variant = "h6" compact="h6">
                        What and Why?
                    </Typography>
                    <Typography variant = "subtitle1" compact="subtitle1">
                        A memory palace is a pre-historic memory technique. Before information was easily accessible and when literacy was only for the educated, history, science, religion and much more was often all carried through generations from one person to another.
                        </Typography>
                        <Grid item xs={12} align="center">
                    <Typography variant = "subtitle1" compact="subtitle1">
                    <br/>
                        Now that information is readily accessible some may consider the pre-historic technique to be just that. 
                    
                        However it's still as incredible a tool today as it ever was. Whether you want to impress your piers by recalling the last 20 nobel piece prze winners, or you are learning your secound, third or even fourth language,an ability to instanly recall vast amounts of information will never go unoticed and may be all you need to land that dream job our to take that next step in your career. 
                        
                        <br />
                        <br/>
                        Alongside that there are also diseases such as Alzheimers to consider. Some studies point towards the possibility that with the progression of Alzheimers a persons musical memory is mostly retained. What if there was the possibility of building a musical memory palace, a memory palce in the form of a song or rythmic poem that could be built by early stage Alzheimers patients and filled with important people from there lives that may allow them to recall names of relatives they may have begun to forget. 

                        This is entirely theoretical yet, the studies into the retention of musical memory are still limited, but it may open a new reserach area into the prevention or treatment of such diseases.
                        <br />
                        <br/>
                    </Typography>
                    </Grid>
                    <Typography variant = "h6" compact="h6">
                        How do I start?
                    </Typography>
                    <Typography variant = "subtitle1" compact="subtitle1">
                        Thats a great question, why not build your own memory palace, just like some of your pre-historic ancestors. 
                        <br />
                        <br/>
                        Find a list of names or things you wish to remember and enter them into the Memory Palace Builder.
                        <br />
                        <br/>
                        The builder will output a list of trigger words. Spend time with those words placing them around a place that is familiar to you in your mind. The more eccentric the image of your palace is in your mind better. 
                        <br />
                        <br/>
            
                        After you build your memory palace, the more often you visit it the more familiar with it you will become and the faster you will be able to recall it. 

                        Add to it as you please and see just how incredible your mind is, push the limits and see just how many things you can fit in your very own personal palace. 
                        <br />
                        <br/>
                    </Typography>
                    <Typography variant = "h6" compact="h6">
                       Also
                    </Typography>
                    <Typography variant = "subtitle1" compact="subtitle1">
                         There are a few different versions to try, make sure you check out the versions page to pick the style that suits you best.
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                <Button color = "secondary" variant ="contained"  to="/" component={Link}>Go Back</Button>
            </Grid>
                <Grid item xs={12} align="center">
            <Button color = "secondary"   to="/versions" component={Link}>About the versions</Button>
            </Grid>
            </Grid>
        </div>
        );
    }
};
