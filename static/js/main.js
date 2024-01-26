function ajaxSelectCoin(coin_name) {
    document.getElementById('coin-information').innerHTML = `
    <canvas class="w-100" id="myChart" style="width: 100%!important; max-width: 700px"></canvas>
        <div id="output-data-container" class="">

            <p2>Output data</p2>
        </div>`
    var currency = document.getElementById('change-currency').value
    $.ajax({
        url: URL_SEND_COIN,
        method: 'post',
        data: {
            'currency': currency,
            'coin_name': coin_name,
            'csrfmiddlewaretoken': TOKEN
        },
        success: function (data) {
            console.log(data)
            var output_cont = document.getElementById('output-data-container')
            output_cont.innerHTML = ''
            let coin_data = data.coin

            console.log(data)
            price_values_for_chart = data.coin['sparkline_in_7d']['price']
            create_chart(price_values_for_chart)
            for (var key in coin_data) {
                output_cont.innerHTML += `<p class="small">${key}: ${coin_data[key]}</p>`

            }
        }
    })
}

function get_coin_follow_url(coin_name) {
    return BASE_URL + `ajax/${coin_name}/add_to_follow`
}

function get_unfollow_url(coin_name) {
    return BASE_URL + `ajax/${coin_name}/unfollow`
}

function ajaxAddToFollow(coin_name) {
    let follow_url = get_coin_follow_url(coin_name)
    $.ajax({
        url: follow_url,
        success: function (ajax_message) {
            console.log(ajax_message)
            let follow_container = document.getElementById('follow-container')
            follow_container.innerHTML +=
                `<div id="${coin_name}_follow_block">
                    <p id="${coin_name}" onClick="ajaxSelectCoin(this.textContent)" style="margin: 5px;">${coin_name}</p>
                    <p id="${coin_name}" onClick="ajaxRemoveFromFollow(this.textContent)" style="margin: 5px;">${coin_name}</p>
                </div>`

        }
    })
}


function create_table(full_data) {

    let i = 1
    if (selected_chat_page === '2') {
        i = 100
    } else if (selected_chat_page === '3') { i = 200}
    let table = document.getElementById('coins-table-body')
    table.innerHTML = null
                for (let key in full_data) {
                        table.innerHTML +=

                            `<th>${i}</th>
                            <td onclick="ajaxAddToFollow(this.textContent)">${full_data[key][1]['id']}</td>
                            <td>${full_data[key][1]['current_price']} ${selected_currency}</td>
                            <td>${full_data[key][1]['market_cap']} ${selected_currency}</td>
                            <td>${full_data[key][1]['total_volume']}</td>
                            <td class="percentage">${full_data[key][1]['price_change_percentage_1h_in_currency']}%</td>
                            <td class="percentage">${full_data[key][1]['price_change_percentage_24h_in_currency']}%</td>
                            <td class="percentage">${full_data[key][1]['price_change_percentage_7d_in_currency']}%</td>`
                        i = i + 1
                        let tds = document.getElementsByClassName('percentage')
                        for (let td of tds) {
                            if (parseFloat(td.innerText) < 0) {
                                td.className = 'table-danger';
                            } else {
                                td.className = 'table-success';
                            }
                        }



                }

}

function ajaxRemoveFromFollow(coin_name) {
    let unfollow_url = get_unfollow_url(coin_name)
    $.ajax({
        url: unfollow_url,
        success: function (ajax_message) {
            console.log(ajax_message)
            let coin_disappear = document.getElementById(`${coin_name}_follow_block`)
            coin_disappear.remove()
        }
    })
}

let selected_currency = 'rub'
let selected_chat_page = '1'

let updateDataPeriodicFunction = setInterval(function () {
    ajaxGetFullData(selected_currency, selected_chat_page)
}, 80000)

document.addEventListener('DOMContentLoaded', function () {
    ajaxGetFullData(selected_currency, selected_chat_page)
})

let coins_data


function ajaxGetFullData(currency, page) {
    selected_currency = currency
    selected_chat_page = page
    $.ajax({
            url: URL_GET_FULL_DATA,
            method: 'post',
            data:
                {
                    'csrfmiddlewaretoken': TOKEN,
                    'currency': currency,
                    'page': page,
                },
            success: function (full_data) {

                let fd = full_data['full_data']
                bubbles = []
                coins_data = fd


                order_table('market_cap')

                drawBubbles(fd, 'market_cap')

            }


        }
    )

}
function drawBubbles (fd, field)
{
    bubbles = []
    let k = getBubbleCoefficient(coins_data, field)
    for (let b in fd) {



                  var radius = parseFloat(fd[b][field]) / k * 150;
                  var x = Math.random() * (canvas.width );
                  var y = Math.random() * (canvas.height);
                  var dx = (Math.random() - 0.5) * 0.5;
                  var dy = (Math.random() - 0.5) * 0.5;
                  var name = `${fd[b]['id']}`
                  var text = `${fd[b][field]}`

                  bubbles.push(new Bubble(x, y, radius, dx, dy, name, text));
                }
}
function getBubbleCoefficient(coins, field) {
    max = 0
    for (let i in coins) {
        console.log(`${field} ${coins[i][field]}`)
        if (parseFloat((coins[i][field])) > max) {
            max = parseFloat(coins[i][field])
        }
    }
    return max
}

function order_table(order_by) {
    let coins_data_array = Object.entries(coins_data);
    coins_data_array.sort(function (a, b) {
        return parseFloat(parseFloat(b[1][order_by] - a[1][order_by]))
    })
    drawBubbles(coins_data, order_by)

    create_table(coins_data_array)




}

//Functions to delete dropped information about selected coin
document.addEventListener('click', function () {
    if (chart !== undefined) {

        document.getElementById('output-data-container').innerHTML = null
    }
})