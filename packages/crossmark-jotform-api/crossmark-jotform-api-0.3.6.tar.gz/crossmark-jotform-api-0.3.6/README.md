# Jotform api library for python3
<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/mirkan1/crossmark-jotform-api/master/logo.png">
</div>

## how to update

## description
specilized library for jotform api and crossmark needs

## updates
- 2023-04-26: added `set_new_submission` function, time to time it cannot find the submission, in that cases pulls the data directly from the api and sets as it is.
- 2023-05-01: added a logic for get_emails function. and added a TODO there.
- 2023-05-01: setted set_answer function.
- 2023-05-10: deleted submissions array and enhanced the logic according to it
- 2023-05-16: created emails on class initilaization so that one dont need to call get_emails function
- 2023-05-16: summary for get_form function, format document, cleared some of the self.update and its fucntionality for faster performance
- 2023-10-20: force parameter for update function so that user can call it without depending on the submission count change, This library need an inner check for the highest updated_at value descending order. 
- 2023-11-08: Unused param selectedFields is omited, added constructer function for answer to smaller parts [maxValue, order, selectedField, cfname, static]
