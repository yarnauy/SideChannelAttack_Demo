#!/usr/bin/env python3


homepageHTML='''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cut To Secret</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap" rel="stylesheet">
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
<style>
    body {
        background-color: #0b3862;
        font-family: Arial, sans-serif;
        color: white;
        cursor: text;
    }
    #container {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }
    #title {
        font-family: 'Poppins', sans-serif;
        font-size: 48px;
        font-weight: bold;
        color: white;
        margin-bottom: 30px;
    }
    #inputBox {
        background-color: transparent;
    }
    #inputField {
        width: 100%;
        padding: 15px;
        font-size: 24px;
        border: none;
        background-color: rgba(0, 0, 0, 0);
        color: white;
        outline: none;
        caret-color: transparent;
        cursor: text;
        position: relative;
        text-align: center;
    }
    #inputField::after {
        content: '|';
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        font-size: 30px;
        color: white;
        animation: blink-caret 0.8s infinite;
    }
    @keyframes blink-caret {
        from, to { color: transparent; }
        50% { color: white; }
    }
    .btn-submit {
        width: 150px;
        font-size: 18px;
        border: 2px solid white;
        border-radius: 5px;
        background-color: transparent;
        color: white;
        transition: all 0.3s ease-in-out;
        margin-top: 10px;
        display: inline-block;
    }
    .btn-submit:hover {
        background-color: white;
        color: #0b3862;
    }
    .correct {
        color: green !important;
    }
    .incorrect {
        color: red !important;
    }
</style>
</head>
<body>
<div id="container">
    <div id="title">Cut to the Secret</div>
    <div id="inputBox" class="container">
        <form>
            <div id="inputField" contenteditable="true" placeholder="Enter a string..." onfocus="clearColor()"></div>
            <br>
            <button type="button" class="btn btn-submit" onclick="checkInput()">Submit</button>
        </form>
    </div>
</div>

<script>

function checkInput() {
    var input = document.getElementById("inputField").innerText;
    var url = "http://47.116.212.124:5000/try?input=" + encodeURIComponent(input);
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.correct) {
                    document.getElementById("inputField").classList.remove("incorrect");
                    document.getElementById("inputField").classList.add("correct");
                } else {
                    document.getElementById("inputField").classList.remove("correct");
                    document.getElementById("inputField").classList.add("incorrect");
                }
            } else {
                alert("Request error. Please try again!");
            }
        }
    };
    xhr.send();
}

function clearColor() {
    document.getElementById("inputField").classList.remove("correct");
    document.getElementById("inputField").classList.remove("incorrect");
}

document.getElementById("inputField").addEventListener("input", function() {
    var inputField = document.getElementById("inputField");
    var text = inputField.innerText;
    var selection = window.getSelection();
    var range = document.createRange();
    range.setStart(inputField.childNodes[0], text.length);
    range.collapse(true);
    selection.removeAllRanges();
    selection.addRange(range);
});
</script>
</body>
</html>
'''
