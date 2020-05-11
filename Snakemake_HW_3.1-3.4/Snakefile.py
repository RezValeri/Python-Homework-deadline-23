SAMPLES = [ "A" ]

print ( "Reading file phase.. #start" )

@workflow.rule(name='all', lineno=5, snakefile='/home/valeri/snakemake_classes/examples/Snakefile')

@workflow.input(
				"plot.svg" ,
				expand ( "peaks/{sample}.bed" , sample = SAMPLES )

)
@workflow.norun()
@workflow.run
def __rule_all(input, output, params, wildcards, threads, resources, log, version, rule, conda_env, singularity_img, singularity_args, use_singularity, bench_record, jobid, is_shell, bench_iteration, shadow_dir):
	pass
@workflow.rule(name='align', lineno=16, snakefile='/home/valeri/snakemake_classes/examples/Snakefile')

@workflow.input( "reads/{sample}.fq.gz"
)

@workflow.output( "bams/{sample}.bam"
)
@workflow.run
def __rule_align(input, output, params, wildcards, threads, resources, log, version, rule, conda_env, singularity_img, singularity_args, use_singularity, bench_record, jobid, is_shell, bench_iteration, shadow_dir):
				print ( "Executing 'align' rule.." )



@workflow.rule(name='call_peaks', lineno=29, snakefile='/home/valeri/snakemake_classes/examples/Snakefile')

@workflow.input( "bams/{sample}.bam"
)

@workflow.output( "peaks/{sample}.bed"
)
@workflow.script ( "scripts/call_peaks.py"

)
@workflow.run
def __rule_call_peaks(input, output, params, wildcards, threads, resources, log, version, rule, conda_env, singularity_img, singularity_args, use_singularity, bench_record, jobid, is_shell, bench_iteration, shadow_dir):
	script ( "scripts/call_peaks.py" , "/home/valeri/snakemake_classes/examples" , input, output, params, wildcards, threads, resources, log, config, rule, conda_env, singularity_img, singularity_args, bench_record, jobid, bench_iteration, shadow_dir
) 


@workflow.rule(name='plot', lineno=45, snakefile='/home/valeri/snakemake_classes/examples/Snakefile')

@workflow.input(
				expand ( "peaks/{sample}.bed" , sample = SAMPLES )
)

@workflow.output( "plot.svg"
)
@workflow.shellcmd ( "echo TODO"

)
@workflow.run
def __rule_plot(input, output, params, wildcards, threads, resources, log, version, rule, conda_env, singularity_img, singularity_args, use_singularity, bench_record, jobid, is_shell, bench_iteration, shadow_dir):
	shell ( "echo TODO" , bench_record=bench_record, bench_iteration=bench_iteration
) 


print ( "Reading file phase.. #end" ) 
Reading file phase.. #start
Reading file phase.. #end
