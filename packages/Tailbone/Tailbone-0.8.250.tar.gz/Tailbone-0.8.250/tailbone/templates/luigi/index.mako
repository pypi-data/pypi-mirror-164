## -*- coding: utf-8; -*-
<%inherit file="/page.mako" />

<%def name="title()">Luigi Jobs</%def>

<%def name="page_content()">
  <br />
  <div class="form">

    <div class="buttons">

      <b-button tag="a"
                % if luigi_url:
                href="${luigi_url}"
                % else:
                href="#" disabled
                title="Luigi URL is not configured"
                % endif
                icon-pack="fas"
                icon-left="external-link-alt"
                target="_blank">
        Luigi Task Visualiser
      </b-button>

      <b-button tag="a"
                % if luigi_history_url:
                href="${luigi_history_url}"
                % else:
                href="#" disabled
                title="Luigi URL is not configured"
                % endif
                icon-pack="fas"
                icon-left="external-link-alt"
                target="_blank">
        Luigi Task History
      </b-button>

      % if master.has_perm('restart_scheduler'):
          ${h.form(url('{}.restart_scheduler'.format(route_prefix)), **{'@submit': 'submitRestartSchedulerForm'})}
          ${h.csrf_token(request)}
          <b-button type="is-primary"
                    native-type="submit"
                    icon-pack="fas"
                    icon-left="redo"
                    :disabled="restartSchedulerFormSubmitting">
            {{ restartSchedulerFormSubmitting ? "Working, please wait..." : "Restart Luigi Scheduler" }}
          </b-button>
          ${h.end_form()}
      % endif
    </div>

    % if master.has_perm('launch'):
        <h3 class="block is-size-3">Overnight Tasks</h3>
        % for task in overnight_tasks:
            <launch-job job-name="${task['key']}"
                        button-text="Restart Overnight ${task['key'].capitalize()}">
            </launch-job>
        % endfor
    % endif

  </div>
</%def>

<%def name="modify_this_page_vars()">
  ${parent.modify_this_page_vars()}
  % if master.has_perm('restart_scheduler'):
      <script type="text/javascript">

        ThisPageData.restartSchedulerFormSubmitting = false

        ThisPage.methods.submitRestartSchedulerForm = function() {
            this.restartSchedulerFormSubmitting = true
        }

      </script>
  % endif
</%def>

<%def name="finalize_this_page_vars()">
  ${parent.finalize_this_page_vars()}
  % if master.has_perm('launch'):
      <script type="text/javascript">

        const LaunchJob = {
            template: '#launch-job-template',
            props: {
                jobName: String,
                buttonText: String,
            },
            data() {
                return {
                    formSubmitting: false,
                }
            },
            methods: {
                submitForm() {
                    this.formSubmitting = true
                },
            },
        }

        Vue.component('launch-job', LaunchJob)

      </script>
  % endif
</%def>

<%def name="render_this_page_template()">
  ${parent.render_this_page_template()}
  % if master.has_perm('launch'):
      <script type="text/x-template" id="launch-job-template">
        ${h.form(url('{}.launch'.format(route_prefix)), method='post', **{'@submit': 'submitForm'})}
        ${h.csrf_token(request)}
        <input type="hidden" name="job" v-model="jobName" />
        <b-button type="is-primary"
                  native-type="submit"
                  :disabled="formSubmitting">
          {{ formSubmitting ? "Working, please wait..." : buttonText }}
        </b-button>
        ${h.end_form()}
      </script>
  % endif
</%def>


${parent.body()}
