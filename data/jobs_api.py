import flask
from flask import jsonify, make_response, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(rules=(
                    '-user.jobs',
                     '-user.hashed_password',
                     '-team_leader.jobs'
                                     ))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': jobs.to_dict(rules=(
                '-user.jobs',
                '-user.hashed_password',
                '-team_leader.jobs'
            )
            )
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job = Jobs(
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators']
    )
    if 'start_date' in request.json:
        job.start_date = request.json['start_date']
    if 'end_date' in request.json:
        job.end_date = request.json['end_date']
    if 'is_finished' in request.json:
        job.is_finished = request.json['is_finished']
    print(job)
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'id': job.id})



@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['POST'])
def edit_job(job_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})

    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)

    if not job:
        return jsonify({'error': 'not found'})

    if 'team_leader' in request.json:
        job.team_leader = request.json['team_leader']
    if 'job' in request.json:
        job.job = request.json['job']
    if 'work_size' in request.json:
        job.work_size = request.json['work_size']
    if 'collaborators' in request.json:
        job.collaborators = request.json['collaborators']
    if 'start_date' in request.json:
        job.start_date = request.json['start_date']
    if 'end_date' in request.json:
        job.end_date = request.json['end_date']
    if 'is_finished' in request.json:
        job.is_finished = request.json['is_finished']

    db_sess.commit()
    return jsonify({'success': 'OK'})
