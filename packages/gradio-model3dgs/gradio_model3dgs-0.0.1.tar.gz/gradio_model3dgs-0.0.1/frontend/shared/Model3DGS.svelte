<script lang="ts">
	import type { FileData } from "@gradio/client";
	import { BlockLabel, IconButton } from "@gradio/atoms";
	import { File, Download } from "@gradio/icons";
	import { onMount } from "svelte";
	import * as SPLAT from "gsplat";
	import type { I18nFormatter } from "@gradio/utils";

	export let value: FileData | null;
	export let label = "";
	export let show_label: boolean;
	export let i18n: I18nFormatter;
	export let zoom_speed = 1;
	export let pan_speed = 1;

	let canvas: HTMLCanvasElement;
	let scene: SPLAT.Scene;
	let camera: SPLAT.Camera;
	let renderer: SPLAT.WebGLRenderer;
	let controls: SPLAT.OrbitControls;
	let mounted = false;

	onMount(() => {
		scene = new SPLAT.Scene();
		camera = new SPLAT.Camera();
		renderer = new SPLAT.WebGLRenderer(canvas);
		controls = new SPLAT.OrbitControls(camera, canvas);
		controls.zoomSpeed = zoom_speed;
		controls.panSpeed = pan_speed;
		console.log("mount");
		console.log(value);
		if(value) {
			console.log(value);
			SPLAT.Loader.LoadFromFileAsync(value.blob, scene, (progress) => {
				console.log(progress);
			});
		}
		window.addEventListener("resize", () => {
			renderer?.resize();
		});
		mounted = true;
	});

	$: ({ path } = value || {
		path: undefined
	});

	$: canvas && mounted && path && dispose();

	function dispose(): void {
		if (renderer !== null) {
			renderer.dispose();
			renderer = new SPLAT.WebGLRenderer(canvas);
			controls = new SPLAT.OrbitControls(camera, canvas);
			controls.zoomSpeed = zoom_speed;
			controls.panSpeed = pan_speed;
			window.addEventListener("resize", () => {
				renderer?.resize();
			});
		}
	}
</script>

<BlockLabel
	{show_label}
	Icon={File}
	label={label || i18n("3DGS_model.splat")}
/>
{#if value}
	<div class="model3DGS">
		<div class="buttons">
			<a
				href={value.path}
				target={window.__is_colab__ ? "_blank" : null}
				download={window.__is_colab__ ? null : value.orig_name || value.path}
			>
				<IconButton Icon={Download} label={i18n("common.download")} />
			</a>
		</div>

		<canvas bind:this={canvas} />
	</div>
{/if}

<style>
	.model3DGS {
		display: flex;
		position: relative;
		width: var(--size-full);
		height: var(--size-full);
	}
	canvas {
		width: var(--size-full);
		height: var(--size-full);
		object-fit: contain;
		overflow: hidden;
	}
	.buttons {
		display: flex;
		position: absolute;
		top: var(--size-2);
		right: var(--size-2);
		justify-content: flex-end;
		gap: var(--spacing-sm);
		z-index: var(--layer-5);
	}
</style>
