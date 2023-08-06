## -*- coding: utf-8; -*-
<%inherit file="/configure.mako" />

<%def name="form_content()">
  ${h.hidden('overnight_tasks', **{':value': 'JSON.stringify(overnightTasks)'})}

  <h3 class="is-size-3">Overnight Tasks</h3>
  <div class="block" style="padding-left: 2rem; display: flex;">

    <b-table :data="overnightTasks">
      <template slot-scope="props">
        <b-table-column field="key"
                        label="Key"
                        sortable>
          {{ props.row.key }}
        </b-table-column>
      </template>
    </b-table>

    <div style="margin-left: 1rem;">
      <b-button type="is-primary"
                icon-pack="fas"
                icon-left="plus"
                @click="overnightTaskCreate()">
        New Task
      </b-button>

      <b-modal has-modal-card
               :active.sync="overnightTaskShowDialog">
        <div class="modal-card">

          <header class="modal-card-head">
            <p class="modal-card-title">Overnight Task</p>
          </header>

          <section class="modal-card-body">
            <b-field label="Key">
              <b-input v-model.trim="overnightTaskKey"
                       ref="overnightTaskKey">
              </b-input>
            </b-field>
          </section>

          <footer class="modal-card-foot">
            <b-button type="is-primary"
                      icon-pack="fas"
                      icon-left="save"
                      @click="overnightTaskSave()"
                      :disabled="!overnightTaskKey">
              Save
            </b-button>
            <b-button @click="overnightTaskShowDialog = false">
              Cancel
            </b-button>
          </footer>
        </div>
      </b-modal>

    </div>
  </div>

  <h3 class="is-size-3">Luigi Proper</h3>
  <div class="block" style="padding-left: 2rem;">

    <b-field label="Luigi URL"
             message="This should be the URL to Luigi Task Visualiser web user interface."
             expanded>
      <b-input name="luigi.url"
               v-model="simpleSettings['luigi.url']"
               @input="settingsNeedSaved = true">
      </b-input>
    </b-field>

    <b-field label="Supervisor Process Name"
             message="This should be the complete name, including group - e.g. luigi:luigid"
             expanded>
      <b-input name="luigi.scheduler.supervisor_process_name"
               v-model="simpleSettings['luigi.scheduler.supervisor_process_name']"
               @input="settingsNeedSaved = true">
      </b-input>
    </b-field>

    <b-field label="Restart Command"
             message="This will run as '${system_user}' system user - please configure sudoers as needed.  Typical command is like:  sudo supervisorctl restart luigi:luigid"
             expanded>
      <b-input name="luigi.scheduler.restart_command"
               v-model="simpleSettings['luigi.scheduler.restart_command']"
               @input="settingsNeedSaved = true">
      </b-input>
    </b-field>

  </div>

</%def>

<%def name="modify_this_page_vars()">
  ${parent.modify_this_page_vars()}
  <script type="text/javascript">

    ThisPageData.overnightTasks = ${json.dumps(overnight_tasks)|n}
    ThisPageData.overnightTaskShowDialog = false
    ThisPageData.overnightTask = null
    ThisPageData.overnightTaskKey = null

    ThisPage.methods.overnightTaskCreate = function() {
        this.overnightTask = null
        this.overnightTaskKey = null
        this.overnightTaskShowDialog = true
        this.$nextTick(() => {
            this.$refs.overnightTaskKey.focus()
        })
    }

    ThisPage.methods.overnightTaskSave = function() {
        if (this.overnightTask) {
            this.overnightTask.key = this.overnightTaskKey
        } else {
            let task = {key: this.overnightTaskKey}
            this.overnightTasks.push(task)
        }
        this.overnightTaskShowDialog = false
        this.settingsNeedSaved = true
    }

  </script>
</%def>


${parent.body()}
