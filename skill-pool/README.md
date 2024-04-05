# Skill pool

Here are snippets used to create the skill-pool.

Might be great to transform that in an internal product at some point (off internal product).

For the redirect url to work, you have to build a page where you will include the skill pull form through an iframe, and add an event on page.
* create a web page on the website
* in the page, add a "Embed Code" block with:
  ```
    <script type="text/javascript">
      window.addEventListener(
        "formioSubmitDone",
        (event) => {
            document.location.href = event.data.submit_done_url;
        },
        false,
      );
    </script>
        <iframe id="formio" src="/formio/public/form/create/FORM-UUID>" width="100%" height="800px" frameborder="0" allowfullscreen="">
    </iframe>
  ```
* use this page for user to edit the form.
