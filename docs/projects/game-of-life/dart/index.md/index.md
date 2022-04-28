---

---

Welcome to the Game Of Life in Dart page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Dart
<!DOCTYPE html>
<html>

<head>
  <script defer src="game-of-life.dart.js"></script>
</head>

<body>
    <h2>Settings</h2>
    <table id="settings">
        <tr>
            <td><label>Width:</label></td>
            <td><input id="width" type="number" value="20" /></td>
        </tr>
        <tr>
            <td id="widthError" class="error" colspan="2"></td>
        </tr>
        <tr>
            <td><label>Height:</label></td>
            <td><input id="height" type="number" value="20" /></td>
        </tr>
        <tr>
            <td id="heightError" class="error" colspan="2"></td>
        </tr>
        <tr>
            <td><label>Wrap:</label></td>
            <td><input id="wrap" type="checkbox" value="checked" checked/></td>
        </tr>
        <tr>
            <td><label>Frame Rate:</label></td>
            <td><input id="frameRate" type="number" value="3" /></td>
        </tr>
        <tr>
            <td id="frameRateError" class="error" colspan="2"></td>
        </tr>
        <tr>
            <td><label>Total Frames:</label></td>
            <td><input id="totalFrames" type="number" value="200" /></td>
        </tr>
        <tr>
            <td id="totalFramesError" class="error" colspan="2"></td>
        </tr>
        <tr>
            <td><label>Spawn Rate (%):</label></td>
            <td><input id="spawnRate" type="number" value="15" /></td>
        </tr>
        <tr>
            <td id="spawnRateError" class="error" colspan="2"></td>
        </tr>
        <tr>
            <td colspan="2">
              <input id="run" type="submit" value="Run" />
              <input id="abort" type="submit" value="Abort" /></td>
            </td>
        </tr>
    </table>
    <br>
    <h2>Board</h2>
    <table id="board"></table>
    <table id="stats">
      <tr>
         <td><label>Frame Number:</label></td>
         <td id="statsFrame"></td>
      </tr>
      <tr>
         <td><label>Living Cells:</label></td>
         <td id="statsLiving"></td>
      </tr>
    </table>
</body>

</html>

<style>
    body {
        background-color: white;
    }
    #board {
        border-collapse: collapse;
        margin: 0px auto;
    }
    td.living {
        background-color: white;
        border: 1px solid silver;
        width: 10px;
        height: 10px;
    }
    td.dead {
        background-color: black;
        border: 1px solid silver;
        width: 10px;
        height: 10px;
    }
    label {
        display: block;
        color: black;
        font-weight: bold;
        text-align: left;
        width: 200px;
    }
    td.error {
        color: red;
    }
</style>

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.