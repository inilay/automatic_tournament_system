
import React from 'react';
import def_tour from "../assets/img/d_t.png" 

const TournamentList = ({tournaments}) => {

    if (!tournaments.length) {
        return (
            <h1 style={{textAlign: 'center'}}>
                Турниры не найдены!
            </h1>
        )
    }

    return (

            <div class="row">
                {tournaments.map((post) =>
                    <div class="col-lg-4 col-md-6 mt-4" key={post.slug}>
                    <div class="card tournament_card">
                    <a href={`/tournament/${post.slug}`}><img src={def_tour} class="card-img-top" alt="card text"/></a>
                    <div class="card-body tournaments_card_body">
                        <h5 class="card-title">{post.title}</h5>
                        <p class="card-text">Game: {post.game}</p>
                        <p class="card-text">Prize: {post.prize}</p>
                    </div>
                    </div>
                    </div>
                )} 
            </div>
          
    );
};

export default TournamentList;